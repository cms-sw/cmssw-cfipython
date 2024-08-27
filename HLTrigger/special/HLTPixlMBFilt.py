import FWCore.ParameterSet.Config as cms

def HLTPixlMBFilt(**kwargs):
  mod = cms.EDFilter('HLTPixlMBFilt',
    saveTags = cms.bool(True),
    pixlTag = cms.InputTag('hltPixelCands'),
    MinPt = cms.double(0),
    MinTrks = cms.uint32(2),
    MinSep = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
