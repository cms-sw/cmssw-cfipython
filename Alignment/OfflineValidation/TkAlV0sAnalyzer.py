import FWCore.ParameterSet.Config as cms

def TkAlV0sAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TkAlV0sAnalyzer',
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    tracks = cms.untracked.InputTag('ALCARECOTkAlKShortTracks'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
