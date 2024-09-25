import FWCore.ParameterSet.Config as cms

def LeptonTaggerByPtESProducer(*args, **kwargs):
  mod = cms.ESProducer('LeptonTaggerByPtESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
