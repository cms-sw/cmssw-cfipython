import FWCore.ParameterSet.Config as cms

def MTDDigiGeometryESModule(*args, **kwargs):
  mod = cms.ESProducer('MTDDigiGeometryESModule',
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
