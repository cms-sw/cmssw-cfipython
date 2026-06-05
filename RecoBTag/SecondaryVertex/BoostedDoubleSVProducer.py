import FWCore.ParameterSet.Config as cms

def BoostedDoubleSVProducer(*args, **kwargs):
  mod = cms.EDProducer('BoostedDoubleSVProducer',
    beta = cms.double(1),
    R0 = cms.double(0.8),
    maxSVDeltaRToJet = cms.double(0.7),
    trackSelection = cms.PSet(),
    trackPairV0Filter = cms.PSet(
      k0sMassWindow = cms.double(0.03)
    ),
    svTagInfos = cms.InputTag('pfInclusiveSecondaryVertexFinderAK8TagInfos'),
    weights = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
