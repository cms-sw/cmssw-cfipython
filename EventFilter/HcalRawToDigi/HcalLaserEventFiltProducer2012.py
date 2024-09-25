import FWCore.ParameterSet.Config as cms

def HcalLaserEventFiltProducer2012(*args, **kwargs):
  mod = cms.EDProducer('HcalLaserEventFiltProducer2012',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
