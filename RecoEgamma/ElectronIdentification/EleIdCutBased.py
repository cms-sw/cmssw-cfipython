import FWCore.ParameterSet.Config as cms

def EleIdCutBased(**kwargs):
  mod = cms.EDFilter('EleIdCutBased',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
