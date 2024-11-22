import FWCore.ParameterSet.Config as cms

def RunInfoTestESProducer(*args, **kwargs):
  mod = cms.ESProducer('RunInfoTestESProducer',
    runInfos = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
