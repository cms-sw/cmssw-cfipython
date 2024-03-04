import FWCore.ParameterSet.Config as cms

def HcalLaserEventFiltProducer2012(**kwargs):
  mod = cms.EDProducer('HcalLaserEventFiltProducer2012',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
