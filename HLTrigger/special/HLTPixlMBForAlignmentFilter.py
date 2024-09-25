import FWCore.ParameterSet.Config as cms

def HLTPixlMBForAlignmentFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTPixlMBForAlignmentFilter',
    saveTags = cms.bool(True),
    pixlTag = cms.InputTag('hltPixelCands'),
    MinPt = cms.double(5),
    MinTrks = cms.uint32(2),
    MinSep = cms.double(1),
    MinIsol = cms.double(0.05),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
