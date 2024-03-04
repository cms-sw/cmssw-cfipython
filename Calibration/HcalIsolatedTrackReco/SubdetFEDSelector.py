import FWCore.ParameterSet.Config as cms

def SubdetFEDSelector(**kwargs):
  mod = cms.EDProducer('SubdetFEDSelector',
    rawInputLabel = cms.InputTag('rawDataCollector'),
    getSiPixel = cms.bool(True),
    getHCAL = cms.bool(True),
    getECAL = cms.bool(False),
    getMuon = cms.bool(False),
    getTrigger = cms.bool(True),
    getSiStrip = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
