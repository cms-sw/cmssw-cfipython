import FWCore.ParameterSet.Config as cms

def CTPPSPixelRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('CTPPSPixelRawToDigi',
    isRun3 = cms.bool(True),
    includeErrors = cms.bool(True),
    inputLabel = cms.InputTag('rawDataCollector'),
    mappingLabel = cms.string('RPix'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
