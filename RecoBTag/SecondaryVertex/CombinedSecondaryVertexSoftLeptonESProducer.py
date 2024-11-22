import FWCore.ParameterSet.Config as cms

def CombinedSecondaryVertexSoftLeptonESProducer(*args, **kwargs):
  mod = cms.ESProducer('CombinedSecondaryVertexSoftLeptonESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
