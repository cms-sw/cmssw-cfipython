import FWCore.ParameterSet.Config as cms

def RunInfoTestESProducer(**kwargs):
  mod = cms.ESProducer('RunInfoTestESProducer',
    runInfos = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
