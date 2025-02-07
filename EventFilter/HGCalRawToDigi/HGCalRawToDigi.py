import FWCore.ParameterSet.Config as cms

def HGCalRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('HGCalRawToDigi',
    src = cms.InputTag('rawDataCollector'),
    fedIds = cms.vuint32(),
    doSerial = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
