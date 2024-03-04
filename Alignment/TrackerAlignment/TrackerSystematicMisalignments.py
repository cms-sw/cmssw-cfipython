import FWCore.ParameterSet.Config as cms

def TrackerSystematicMisalignments(**kwargs):
  mod = cms.EDAnalyzer('TrackerSystematicMisalignments',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
