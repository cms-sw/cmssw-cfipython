import FWCore.ParameterSet.Config as cms

def CTPPSProtonReconstructionValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSProtonReconstructionValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
