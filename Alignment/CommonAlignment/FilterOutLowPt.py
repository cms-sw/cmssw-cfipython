import FWCore.ParameterSet.Config as cms

def FilterOutLowPt(**kwargs):
  mod = cms.EDFilter('FilterOutLowPt',
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    runControl = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(0),
    ptmin = cms.untracked.double(3),
    thresh = cms.untracked.int32(1),
    src = cms.untracked.InputTag('generalTracks'),
    runControlNumber = cms.untracked.vuint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
