import FWCore.ParameterSet.Config as cms

def HLTPixlMBFilt(*args, **kwargs):
  mod = cms.EDFilter('HLTPixlMBFilt',
    saveTags = cms.bool(True),
    pixlTag = cms.InputTag('hltPixelCands'),
    MinPt = cms.double(0),
    MinTrks = cms.uint32(2),
    MinSep = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
