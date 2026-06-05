import FWCore.ParameterSet.Config as cms

def Onia2MuMuPAT(*args, **kwargs):
  mod = cms.EDProducer('Onia2MuMuPAT',
    muons = cms.required.InputTag,
    beamSpotTag = cms.required.InputTag,
    primaryVertexTag = cms.required.InputTag,
    higherPuritySelection = cms.required.string,
    lowerPuritySelection = cms.required.string,
    dimuonSelection = cms.string(''),
    addCommonVertex = cms.required.bool,
    addMuonlessPrimaryVertex = cms.required.bool,
    resolvePileUpAmbiguity = cms.required.bool,
    addMCTruth = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
