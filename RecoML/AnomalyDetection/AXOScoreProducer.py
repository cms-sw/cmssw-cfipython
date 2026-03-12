import FWCore.ParameterSet.Config as cms

def AXOScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('AXOScoreProducer',
    pfCandidates = cms.InputTag('hltParticleFlow'),
    muons = cms.InputTag('hltIterL3MuonsNoVtx'),
    egammaCands = cms.InputTag('hltEgammaCandidates'),
    gsfTracks = cms.InputTag('hltEgammaGsfTracks'),
    vertices = cms.InputTag('hltPixelVertices'),
    modelPath = cms.FileInPath('HLTrigger/HLTfilters/data/hlt_ad_model.pt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
