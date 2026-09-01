import FWCore.ParameterSet.Config as cms

def TICLCandidateExtraTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TICLCandidateExtraTableProducer',
    name = cms.required.string,
    doc = cms.string(''),
    extension = cms.bool(False),
    skipNonExistingSrc = cms.bool(False),
    src = cms.required.InputTag,
    variables = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        expr = cms.required.string,
        doc = cms.required.string,
        lazyEval = cms.untracked.bool(False),
        type = cms.string('int')
      )
    ),
    tracksters = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    tracks = cms.InputTag('generalTracks'),
    linkedTracksters = cms.optional.InputTag,
    caloParticles = cms.optional.InputTag,
    caloParticleToSimClustersMap = cms.optional.InputTag,
    detector = cms.string('HGCAL'),
    propagator = cms.string('PropagatorWithMaterial'),
    produceGeneralTrackBoundary = cms.bool(False),
    collectionVariables = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
