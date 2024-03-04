import FWCore.ParameterSet.Config as cms

def CTPPSPixelRawToDigi(**kwargs):
  mod = cms.EDProducer('CTPPSPixelRawToDigi',
    isRun3 = cms.bool(True),
    includeErrors = cms.bool(True),
    inputLabel = cms.InputTag('rawDataCollector'),
    mappingLabel = cms.string('RPix'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
