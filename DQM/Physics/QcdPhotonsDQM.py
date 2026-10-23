import FWCore.ParameterSet.Config as cms

def QcdPhotonsDQM(*args, **kwargs):
  mod = cms.EDProducer('QcdPhotonsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
