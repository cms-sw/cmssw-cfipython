import FWCore.ParameterSet.Config as cms

RecoTauCleaner = cms.EDProducer('RecoTauCleaner',
  outputSelection = cms.string(''),
  cleaners = cms.VPSet(
    cms.PSet(
      name = cms.string('Charge'),
      nprongs = cms.vuint32(
        1,
        3
      ),
      passForCharge = cms.int32(1),
      plugin = cms.string('RecoTauChargeCleanerPlugin'),
      selectionFailValue = cms.double(0),
      tolerance = cms.double(0)
    ),
    cms.PSet(
      name = cms.string('HPS_Select'),
      plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
      src = cms.InputTag('hpsSelectionDiscriminator'),
      tolerance = cms.double(0)
    ),
    cms.PSet(
      minTrackPt = cms.double(5),
      name = cms.string('killSoftTwoProngTaus'),
      plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
      tolerance = cms.double(0)
    ),
    cms.PSet(
      name = cms.string('ChargedHadronMultiplicity'),
      plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
      tolerance = cms.double(0)
    ),
    cms.PSet(
      name = cms.string('Pt'),
      plugin = cms.string('RecoTauStringCleanerPlugin'),
      selection = cms.string('leadPFCand().isNonnull()'),
      selectionFailValue = cms.double(1000),
      selectionPassFunction = cms.string('-pt()'),
      tolerance = cms.double(0.01)
    ),
    cms.PSet(
      name = cms.string('StripMultiplicity'),
      plugin = cms.string('RecoTauStringCleanerPlugin'),
      selection = cms.string('leadPFCand().isNonnull()'),
      selectionFailValue = cms.double(1000),
      selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
      tolerance = cms.double(0)
    ),
    cms.PSet(
      name = cms.string('CombinedIsolation'),
      plugin = cms.string('RecoTauStringCleanerPlugin'),
      selection = cms.string('leadPFCand().isNonnull()'),
      selectionFailValue = cms.double(1000),
      selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
      tolerance = cms.double(0)
    )
  ),
  verbosity = cms.int32(0),
  src = cms.InputTag('combinatoricRecoTaus')
)
