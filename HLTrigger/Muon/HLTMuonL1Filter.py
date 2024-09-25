import FWCore.ParameterSet.Config as cms

def HLTMuonL1Filter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonL1Filter',
    saveTags = cms.bool(True),
    CandTag = cms.InputTag('hltL1extraParticles'),
    PreviousCandTag = cms.InputTag(''),
    MaxEta = cms.double(2.5),
    MinPt = cms.double(0),
    MinN = cms.int32(1),
    ExcludeSingleSegmentCSC = cms.bool(False),
    CSCTFtag = cms.InputTag('csctfDigis'),
    SelectQualities = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
