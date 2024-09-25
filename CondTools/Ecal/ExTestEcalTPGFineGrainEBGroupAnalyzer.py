import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGFineGrainEBGroupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGFineGrainEBGroupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
