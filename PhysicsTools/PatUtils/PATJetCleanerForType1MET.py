import FWCore.ParameterSet.Config as cms

def PATJetCleanerForType1MET(**kwargs):
  mod = cms.EDProducer('PATJetCleanerForType1MET',
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
