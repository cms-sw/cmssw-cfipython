import FWCore.ParameterSet.Config as cms

def ShiftedPATPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPATPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
