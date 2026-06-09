import FWCore.ParameterSet.Config as cms

def LhcTrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LhcTrackAnalyzer',
    TrackCollectionTag = cms.InputTag('ALCARECOTkAlMinBias'),
    PVtxCollectionTag = cms.InputTag('offlinePrimaryVertices'),
    Debug = cms.bool(False),
    acceptedBX = cms.vuint32(),
    OutputFileName = cms.string('LhcTrackAnalyzer_Output_default.root'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
