import FWCore.ParameterSet.Config as cms

def ManyIntProducer(*args, **kwargs):
  mod = cms.EDProducer('ManyIntProducer',
    ivalue = cms.required.int32,
    throw = cms.untracked.bool(False),
    values = cms.VPSet(
    ),
    transientValues = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
