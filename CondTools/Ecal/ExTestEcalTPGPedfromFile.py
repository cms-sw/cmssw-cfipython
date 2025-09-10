import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPedfromFile(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPedfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
