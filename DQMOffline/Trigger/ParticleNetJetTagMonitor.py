import FWCore.ParameterSet.Config as cms

def ParticleNetJetTagMonitor(*args, **kwargs):
  mod = cms.EDProducer('ParticleNetJetTagMonitor',
    FolderName = cms.string('HLT/Higgs'),
    requireValidHLTPaths = cms.bool(True),
    requireHLTOfflineJetMatching = cms.bool(True),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    muons = cms.InputTag('muons'),
    electrons = cms.InputTag('gedGsfElectrons'),
    tagElectronID = cms.InputTag('egmGsfElectronIDsForDQM', 'cutBasedElectronID-RunIIIWinter22-V1-tight'),
    vetoElectronID = cms.InputTag('egmGsfElectronIDsForDQM', 'cutBasedElectronID-RunIIIWinter22-V1-loose'),
    jets = cms.InputTag('ak4PFJetsCHS'),
    jetPNETScore = cms.InputTag('pfParticleNetAK4DiscriminatorsJetTags', 'BvsAll'),
    jetPNETScoreHLT = cms.InputTag('hltParticleNetDiscriminatorsJetTags', 'BvsAll'),
    jetsForHTandBTag = cms.InputTag(''),
    jetPNETScoreForHTandBTag = cms.InputTag(''),
    jetSoftDropMass = cms.InputTag(''),
    met = cms.InputTag('pfMetPuppi'),
    jecForMC = cms.InputTag('ak4PFCHSL1FastL2L3Corrector'),
    jecForData = cms.InputTag('ak4PFCHSL1FastL2L3ResidualCorrector'),
    tagMuonSelection = cms.string('pt > 25 && abs(eta) < 2.4 && passed(CutBasedIdTight) && passed(PFIsoTight)'),
    tagElectronSelection = cms.string('pt > 20 && abs(eta) < 2.5'),
    vetoMuonSelection = cms.string('pt > 10 && abs(eta) < 2.4 && passed(CutBasedIdLoose) && passed(PFIsoLoose)'),
    vetoElectronSelection = cms.string('pt > 10 && abs(eta) < 2.5'),
    jetSelection = cms.string('pt > 30 && abs(eta) < 2.5'),
    jetSelectionForHTandBTag = cms.string('pt > 30 && abs(eta) < 2.5'),
    vertexSelection = cms.string('!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2'),
    dileptonSelection = cms.string('((mass > 20 && mass < 75) || mass > 105) && charge == 0'),
    metSelection = cms.string('pt > 0'),
    ntagleptons = cms.int32(2),
    ntagmuons = cms.int32(1),
    ntagelectrons = cms.int32(1),
    nvetoleptons = cms.int32(2),
    nvetomuons = cms.int32(1),
    nvetoelectrons = cms.int32(1),
    nemupairs = cms.int32(1),
    njets = cms.int32(2),
    nbjets = cms.int32(-1),
    ntrigobjecttomatch = cms.uint32(2),
    lepJetDeltaRmin = cms.double(0.4),
    lepJetDeltaRminForHTandBTag = cms.double(0.4),
    hltRecoDeltaRmax = cms.double(0.4),
    maxLeptonDxyCut = cms.double(0.1),
    maxLeptonDzCut = cms.double(0.2),
    minPNETScoreCut = cms.double(0.2),
    minPNETBTagCut = cms.double(0.5),
    minSoftDropMassCut = cms.double(50),
    maxSoftDropMassCut = cms.double(110),
    leptonPtBinning = cms.vdouble(),
    leptonEtaBinning = cms.vdouble(),
    diLeptonPtBinning = cms.vdouble(),
    diLeptonMassBinning = cms.vdouble(),
    HTBinning = cms.vdouble(),
    NjetBinning = cms.vdouble(),
    jet1PtBinning = cms.vdouble(),
    jet2PtBinning = cms.vdouble(),
    jet1EtaBinning = cms.vdouble(),
    jet2EtaBinning = cms.vdouble(),
    jet1PNETscoreBinning = cms.vdouble(),
    jet2PNETscoreBinning = cms.vdouble(),
    jet1PNETscoreTransBinning = cms.vdouble(),
    jet2PNETscoreTransBinning = cms.vdouble(),
    jet1PtBinning2d = cms.vdouble(),
    jet2PtBinning2d = cms.vdouble(),
    jet1EtaBinning2d = cms.vdouble(),
    jet2EtaBinning2d = cms.vdouble(),
    jet1PNETscoreBinning2d = cms.vdouble(),
    jet2PNETscoreBinning2d = cms.vdouble(),
    jet1PNETscoreTransBinning2d = cms.vdouble(),
    jet2PNETscoreTransBinning2d = cms.vdouble(),
    numGenericTriggerEvent = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    denGenericTriggerEvent = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
