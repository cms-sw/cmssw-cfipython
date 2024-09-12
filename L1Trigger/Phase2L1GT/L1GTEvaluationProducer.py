import FWCore.ParameterSet.Config as cms

def L1GTEvaluationProducer(**kwargs):
  mod = cms.EDProducer('L1GTEvaluationProducer',
    random_seed = cms.optional.untracked.uint32,
    maxFrames = cms.untracked.uint32(1024),
    inputFilename = cms.required.untracked.string,
    inputFileExtension = cms.untracked.string('txt'),
    outputFilename = cms.required.untracked.string,
    outputFileExtension = cms.untracked.string('txt'),
    patternFormat = cms.untracked.string('EMPv2'),
    InputChannels = cms.untracked.PSet(
      GCT_1 = cms.required.untracked.vuint32,
      GMT_1 = cms.required.untracked.vuint32,
      GTT_1 = cms.required.untracked.vuint32,
      GTT_2 = cms.required.untracked.vuint32,
      GTT_3 = cms.required.untracked.vuint32,
      GTT_4 = cms.required.untracked.vuint32,
      CL2_1 = cms.required.untracked.vuint32,
      CL2_2 = cms.required.untracked.vuint32,
      CL2_3 = cms.required.untracked.vuint32
    ),
    OutputChannels = cms.untracked.PSet(
      GTTPromptJets = cms.optional.untracked.vuint32,
      GTTDisplacedJets = cms.optional.untracked.vuint32,
      GTTPromptHtSum = cms.optional.untracked.vuint32,
      GTTDisplacedHtSum = cms.optional.untracked.vuint32,
      GTTEtSum = cms.optional.untracked.vuint32,
      GTTHadronicTaus = cms.optional.untracked.vuint32,
      CL2JetsSC4 = cms.optional.untracked.vuint32,
      CL2JetsSC8 = cms.optional.untracked.vuint32,
      CL2Taus = cms.optional.untracked.vuint32,
      CL2HtSum = cms.optional.untracked.vuint32,
      CL2EtSum = cms.optional.untracked.vuint32,
      GCTNonIsoEg = cms.optional.untracked.vuint32,
      GCTIsoEg = cms.optional.untracked.vuint32,
      GCTJets = cms.optional.untracked.vuint32,
      GCTTaus = cms.optional.untracked.vuint32,
      GCTHtSum = cms.optional.untracked.vuint32,
      GCTEtSum = cms.optional.untracked.vuint32,
      GMTSaPromptMuons = cms.optional.untracked.vuint32,
      GMTSaDisplacedMuons = cms.optional.untracked.vuint32,
      GMTTkMuons = cms.optional.untracked.vuint32,
      GMTTopo = cms.optional.untracked.vuint32,
      CL2Electrons = cms.optional.untracked.vuint32,
      CL2Photons = cms.optional.untracked.vuint32,
      GTTPhiCandidates = cms.optional.untracked.vuint32,
      GTTRhoCandidates = cms.optional.untracked.vuint32,
      GTTBsCandidates = cms.optional.untracked.vuint32,
      GTTPromptTracks = cms.optional.untracked.vuint32,
      GTTDisplacedTracks = cms.optional.untracked.vuint32,
      GTTPrimaryVert = cms.optional.untracked.vuint32
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
