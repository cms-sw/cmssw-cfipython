import FWCore.ParameterSet.Config as cms

def LhcTrackAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LhcTrackAnalyzer',
    TrackCollectionTag = cms.InputTag('ALCARECOTkAlMinBias'),
    PVtxCollectionTag = cms.InputTag('offlinePrimaryVertices'),
    Debug = cms.bool(False),
    acceptedBX = cms.vuint32(),
    OutputFileName = cms.string('LhcTrackAnalyzer_Output_default.root'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
