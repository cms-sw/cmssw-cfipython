import FWCore.ParameterSet.Config as cms

def MLPFProducer(*args, **kwargs):
  mod = cms.EDProducer('MLPFProducer',
    src = cms.InputTag('particleFlowBlock'),
    model_path = cms.FileInPath('RecoParticleFlow/PFProducer/data/mlpf/mlpf_5M_attn2x3x256_bm12_relu_checkpoint10_8xmi250_fp32_fused_20250722.onnx'),
    additionalTrackFilterNoHCAL = cms.bool(False),
    AdditionalTrackFilterNoHCALParams = cms.PSet(
      additionalFilterTk = cms.string('1.48 < abs(eta) < 3.0'),
      pt_Error = cms.double(1)
    ),
    noRegressionEndcap = cms.bool(False),
    endcapTk = cms.string('1.48 < abs(eta) < 3.0'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
