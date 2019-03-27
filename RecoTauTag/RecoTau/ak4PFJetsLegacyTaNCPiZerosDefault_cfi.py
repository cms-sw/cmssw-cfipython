import FWCore.ParameterSet.Config as cms

ak4PFJetsLegacyTaNCPiZerosDefault = cms.EDProducer('RecoTauPiZeroProducer',
  massHypothesis = cms.double(0.136),
  ranking = cms.VPSet(
    cms.PSet(
      name = cms.string(''),
      plugin = cms.string(''),
      selection = cms.string(''),
      selectionFailValue = cms.double(1000),
      selectionPassFunction = cms.string('')
    )
  ),
  verbosity = cms.int32(0),
  maxJetAbsEta = cms.double(2.5),
  outputSelection = cms.string('pt > 1.5'),
  minJetPt = cms.double(14),
  jetSrc = cms.InputTag('ak4PFJets'),
  builders = cms.VPSet(
    cms.PSet(
      name = cms.string(''),
      plugin = cms.string(''),
      verbosity = cms.int32(0)
    )
  )
)
