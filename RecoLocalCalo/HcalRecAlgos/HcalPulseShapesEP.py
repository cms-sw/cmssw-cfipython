import FWCore.ParameterSet.Config as cms

def HcalPulseShapesEP(*args, **kwargs):
  mod = cms.ESProducer('HcalPulseShapesEP',
    productLabel = cms.string('HcalDataShapes'),
    pulseShapeLength = cms.uint32(250),
    globalTimeShift = cms.double(0),
    pulseDumpFile = cms.untracked.string(''),
    dumpPrecision = cms.untracked.uint32(6),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
