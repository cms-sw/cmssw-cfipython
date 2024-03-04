import FWCore.ParameterSet.Config as cms

def ManyIntProducer(**kwargs):
  mod = cms.EDProducer('ManyIntProducer',
    ivalue = cms.required.int32,
    throw = cms.untracked.bool(False),
    values = cms.VPSet(
    ),
    transientValues = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
