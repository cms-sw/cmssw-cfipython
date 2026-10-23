import FWCore.ParameterSet.Config as cms

def HLTCSCRing2or3Filter(*args, **kwargs):
  mod = cms.EDFilter('HLTCSCRing2or3Filter',
    saveTags = cms.bool(True),
    input = cms.InputTag('hltCsc2DRecHits'),
    minHits = cms.uint32(4),
    xWindow = cms.double(2),
    yWindow = cms.double(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
