"""Merge independently maintained editorial records without duplicating rows."""
import csv
from corpus import RESULT, write_tsv

HEADERS={
 'CAMBIOS':['file','place','before','after','kind','source'],
 'TRADUCCION':['file','french_source','range','words'],
 'HECHO_REVISADO':['id','file','place','verdict','reason'],
 'GLOSARIO_REGISTRO':['french_term','spanish_rendering','witness','places','reversible'],
 'ESTANDAR_APLICADO':['row','found','changed','places_left','reason'],
 'CHECK_EVENTS':['statement_id','date','who','type','outcome'],
}
CHANGE_KINDS={'correction carried','respelling','standard','own comparison','assembly'}
# Retained under their checkpoint names for documentary continuity only.
# III is consolidated in CAMBIOS_iii.tsv; the old standard proposals are fully
# represented by the two CAMBIOS_standard_model_applied_* records.
HISTORICAL_CHANGE_RECORDS={
    'CAMBIOS_iii_manual.tsv',
    'CAMBIOS_iii_math_aligned.tsv',
    'CAMBIOS_standard_model.tsv',
}
BACKGROUND='carried as background without fault found'
CHECK_TYPES={'targeted proof check','independent re-proof','computation or formal certificate',
             'used and rechecked in this run',BACKGROUND}

def normalize(prefix,row,record_file,line,normalizations):
    """Normalize the final schema, retaining original metadata in history."""
    row=dict(row)
    def set_field(field,value):
        if row.get(field,'')!=value:
            normalizations.append([record_file.name,line,field,row.get(field,''),value])
            row[field]=value
    if prefix=='CAMBIOS' and row['kind'] not in CHANGE_KINDS:
        old=row['kind']
        if any(x in old.lower() for x in ['terminolog','standard']):kind='standard'
        elif any(x in old.lower() for x in ['order','page marker','page_marker','pagemarker']):kind='assembly'
        else:kind='own comparison'
        set_field('kind',kind)
        set_field('source',row['source']+'; previous record kind: '+old)
    if prefix=='CHECK_EVENTS':
        old_type=row['type']
        textual_certificate=(old_type=='computation or formal certificate' and
            (record_file.name=='CHECK_EVENTS_iv1_section1.tsv' or
             'literal_TeX_stream' in row['statement_id'] or
             row['outcome'].startswith('Textual computation only:')))
        invalid_type=old_type not in CHECK_TYPES and not old_type.startswith('refuted,')
        if textual_certificate or invalid_type:
            set_field('type',BACKGROUND)
            set_field('outcome','Textual/editorial source comparison only; no mathematical proof verified. '
                      +row['outcome']+' Previous event type: '+old_type+'.')
        old_who=row['who']
        if old_who.lower()=='script':
            who=('Deterministic script under GPT-6 Astra; OpenAI; ChatGPT Pro mode; '
                 'effort not exposed; final EGA_ES_FINISH run; script-only textual/structural comparison')
        elif old_who=='IA':
            who=('GPT-6 Astra; OpenAI; ChatGPT Pro mode; effort not exposed; '
                 'final EGA_ES_FINISH source-comparison run; prior metadata: IA')
        else:
            who=old_who
            if 'OpenAI' not in who:who+='; OpenAI'
            if 'ChatGPT Pro' not in who:who+='; ChatGPT Pro mode'
            if 'effort' not in who.lower():who+='; effort not exposed'
        set_field('who',who)
    return row

def main():
    normalizations=[]
    for prefix,header in HEADERS.items():
        rows=[];seen=set()
        for p in sorted((RESULT/'records').glob(prefix+'_*.tsv')):
            if p.name in HISTORICAL_CHANGE_RECORDS:continue
            if prefix=='ESTANDAR_APLICADO' and p.name!='ESTANDAR_APLICADO_final.tsv':continue
            if prefix=='GLOSARIO_REGISTRO' and p.name.startswith('GLOSARIO_REGISTRO_held') and p.name!='GLOSARIO_REGISTRO_held_final_verify.tsv':continue
            if p.name.startswith('CAMBIOS_ch0_'):continue
            if p.name.startswith('TRADUCCION_iv4_remaining_errata_quotes'):continue
            with p.open(newline='') as f:
                reader=csv.DictReader(f,delimiter='\t')
                if reader.fieldnames!=header:raise ValueError('Unexpected columns in '+p.name+': '+str(reader.fieldnames))
                for line,row in enumerate(reader,2):
                    row=normalize(prefix,row,p,line,normalizations)
                    values=tuple(row.get(k,'') for k in header)
                    if values not in seen:rows.append(values);seen.add(values)
        write_tsv(RESULT/(prefix+'.tsv'),header,rows)
        print(prefix,len(rows))
    write_tsv(RESULT/'records/MERGE_NORMALIZATION.tsv',
              ['record_file','record_line','field','before','after'],normalizations)
if __name__=='__main__':main()
