import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionValidator(**kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
