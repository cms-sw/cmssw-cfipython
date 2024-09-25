import FWCore.ParameterSet.Config as cms

def SingleTopTChannelLeptonDQM_miniAOD(*args, **kwargs):
  mod = cms.EDProducer('SingleTopTChannelLeptonDQM_miniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
