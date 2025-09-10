import FWCore.ParameterSet.Config as cms

def LeptonTaggerByDistanceESProducer(*args, **kwargs):
  mod = cms.ESProducer('LeptonTaggerByDistanceESProducer',
    distance = cms.double(0.5),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
