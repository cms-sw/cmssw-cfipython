import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainTowerfromFile(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainTowerfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
