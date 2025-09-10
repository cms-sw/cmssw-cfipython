import FWCore.ParameterSet.Config as cms

def SubdetFEDSelector(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
