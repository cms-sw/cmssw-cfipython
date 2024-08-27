import FWCore.ParameterSet.Config as cms

def SingleTopTChannelLeptonDQM_miniAOD(**kwargs):
  mod = cms.EDProducer('SingleTopTChannelLeptonDQM_miniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
