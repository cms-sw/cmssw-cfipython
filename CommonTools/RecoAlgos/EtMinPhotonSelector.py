import FWCore.ParameterSet.Config as cms

def EtMinPhotonSelector(**kwargs):
  mod = cms.EDFilter('EtMinPhotonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
