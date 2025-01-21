import FWCore.ParameterSet.Config as cms

def StripCPEESProducer(*args, **kwargs):
  mod = cms.ESProducer('StripCPEESProducer',
    ComponentName = cms.string('SimpleStripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
