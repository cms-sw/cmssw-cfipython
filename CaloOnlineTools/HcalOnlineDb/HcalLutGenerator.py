import FWCore.ParameterSet.Config as cms

def HcalLutGenerator(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLutGenerator',
    tag = cms.string('NewLutTag'),
    HO_master_file = cms.string('HO_ped9_inputLUTcoderDec.txt'),
    status_word_to_mask = cms.uint32(32768),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
