import FWCore.ParameterSet.Config as cms

def HLTADFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTADFilter',
    pfCandidates = cms.InputTag('hltParticleFlow'),
    muons = cms.InputTag('hltIterL3MuonsNoVtx'),
    egammaCands = cms.InputTag('hltEgammaCandidates'),
    gsfTracks = cms.InputTag('hltEgammaGsfTracks'),
    vertices = cms.InputTag('hltPixelVertices'),
    modelPath = cms.FileInPath('HLTrigger/HLTfilters/data/hlt_ad_model.pt'),
    threshold = cms.double(21.499275),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
