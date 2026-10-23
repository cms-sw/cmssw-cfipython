import FWCore.ParameterSet.Config as cms

def PATPFJetMETcorrInputProducer(*args, **kwargs):
  mod = cms.EDProducer('PATPFJetMETcorrInputProducer',
    src = cms.InputTag('ak4PFJetsCHS'),
    offsetCorrLabel = cms.InputTag('ak4PFCHSL1FastjetCorrector'),
    jetCorrLabel = cms.InputTag('ak4PFCHSL1FastL2L3Corrector'),
    jetCorrLabelRes = cms.InputTag('ak4PFCHSL1FastL2L3ResidualCorrector'),
    jetCorrEtaMax = cms.double(9.9),
    type1JetPtThreshold = cms.double(15),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuons = cms.bool(True),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
