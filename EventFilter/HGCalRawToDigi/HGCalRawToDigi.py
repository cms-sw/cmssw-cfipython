import FWCore.ParameterSet.Config as cms

def HGCalRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('HGCalRawToDigi',
    src = cms.InputTag('rawDataCollector'),
    doSerial = cms.bool(True),
    headersOnly = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
