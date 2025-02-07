import FWCore.ParameterSet.Config as cms

def PFJetCleanerForType1MET(*args, **kwargs):
  mod = cms.EDProducer('PFJetCleanerForType1MET',
    src = cms.required.InputTag,
    offsetCorrLabel = cms.required.InputTag,
    jetCorrLabel = cms.required.InputTag,
    jetCorrLabelRes = cms.required.InputTag,
    jetCorrEtaMax = cms.double(9.9),
    type1JetPtThreshold = cms.required.double,
    skipEM = cms.required.bool,
    skipEMfractionThreshold = cms.required.double,
    skipMuons = cms.required.bool,
    skipMuonSelection = cms.required.string,
    calcMuonSubtrRawPtAsValueMap = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
